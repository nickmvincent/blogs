#!/usr/bin/env python3
"""Preview or explicitly deploy the blogs build to the existing Pages repository."""
import argparse
import json
from pathlib import Path
import shutil
import subprocess
import tempfile

from build_garden import ROOT, build


def run(args, cwd=ROOT):
    return subprocess.check_output(args, cwd=cwd, text=True).strip()


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--apply', action='store_true', help='Commit and push the reviewed public site')
    args=parser.parse_args()
    config=json.loads((ROOT/'site/garden.json').read_text())
    if args.apply:
        if run(['git','status','--porcelain']):
            raise SystemExit('Commit the reviewed blogs changes before deploying.')
        local=run(['git','rev-parse','HEAD'])
        remote=run(['git','ls-remote','origin','refs/heads/'+config['source_branch']]).split()
        if not remote or remote[0]!=local:
            raise SystemExit('The build must come from the current pushed source branch: '+config['source_branch'])
    build()
    with tempfile.TemporaryDirectory(prefix='blogs-pages-') as directory:
        checkout=Path(directory)/'pages'
        subprocess.run(['gh','repo','clone',config['pages_repository'],str(checkout),'--',
                        '--depth','1','--branch',config['pages_branch']],check=True)
        # This is a disposable clone. Preserve repository workflows, custom-domain
        # configuration, and verification files; replace only the generated site.
        for path in checkout.iterdir():
            if path.name in {'.git','.github','CNAME','.well-known'}:continue
            if path.is_dir() and not path.is_symlink():shutil.rmtree(path)
            else:path.unlink()
        for path in (ROOT/'_site').iterdir():
            target=checkout/path.name
            if path.is_dir():shutil.copytree(path,target,dirs_exist_ok=True)
            else:shutil.copy2(path,target)
        run(['git','add','-A'],checkout)
        changes=run(['git','diff','--cached','--stat'],checkout)
        print(changes or 'The deployed site already matches the build.')
        report={'source_repository':config['source_url'],'source_commit':run(['git','rev-parse','HEAD']),
                'target_repository':config['pages_repository'],'target_branch':config['pages_branch'],
                'diff_stat':changes,'applied':False}
        cache=ROOT/'.import-cache';cache.mkdir(exist_ok=True)
        (cache/'deployment-preview.json').write_text(json.dumps(report,indent=2)+'\n')
        if not args.apply:
            print('Preview only. No commit or push was made.')
            return
        if changes:
            run(['git','commit','-m','Deploy Data Leverage garden from blogs '+report['source_commit'][:12]],checkout)
            run(['git','push','origin',config['pages_branch']],checkout)
            report['applied']=True
            (cache/'deployment-preview.json').write_text(json.dumps(report,indent=2)+'\n')
            print('Deployed to '+config['url'])


if __name__=='__main__':main()
