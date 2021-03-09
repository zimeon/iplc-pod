#!/usr/bin/env python3
"""
Script to upload metadata to POD

Simeon Warner / 2021-03-09
"""
import argparse
import subprocess

parser = argparse.ArgumentParser(description='Upload data to POD.')
parser.add_argument('--endpoint', type=str,
                    default='https://pod.stanford.edu/organizations/cornell/uploads',
                    help="endpoint URL to POST data to")
parser.add_argument('--token', type=str, required=True,
                    help="bearer authentication token for upload (get from upload page)")
parser.add_argument('files', nargs='+', type=str,
                    help="names of files to upload")
args = parser.parse_args()

for file in args.files:
    print("Uploading %s" % (file))
    subprocess.run(['curl',
                    '-F', 'upload[name]=%s' % file,
                    '-F', 'upload[files][]=@%s;type=application/gzip' % file,
                    '-H', 'Authorization: Bearer ' + args.token,
                    args.endpoint])
