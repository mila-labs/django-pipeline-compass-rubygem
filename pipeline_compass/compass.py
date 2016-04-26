from os.path import dirname
from django.conf import settings

from pipeline.compilers import SubProcessCompiler

class CompassCompiler(SubProcessCompiler):
    output_extension = 'css'

    def match_file(self, filename):
        return filename.endswith(('.scss', '.sass'))

    def compile_file(self, infile, outfile, outdated=False, force=False):
        conf = getattr(settings, 'PIPELINE', {})
        command = [
            conf.get('COMPASS_BINARY', ['/usr/bin/env', 'compass']),
            "compile", "--boring",
            "--sass-dir=%s" % dirname(infile),
            "--css-dir=%s" % dirname(outfile),
            conf.get('COMPASS_ARGUMENTS', []),
            infile
        ]
        return self.execute_command(command, cwd=dirname(infile))
