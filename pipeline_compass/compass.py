from os.path import dirname
from django.conf import settings

from pipeline.compilers import SubProcessCompiler

class CompassCompiler(SubProcessCompiler):
    output_extension = 'css'

    def match_file(self, filename):
        return filename.endswith(('.scss', '.sass'))

    def compile_file(self, infile, outfile, outdated=False, force=False):
        command = "%s compile --sass-dir=%s --css-dir=%s %s %s" % (
            getattr(settings, 'PIPELINE_COMPASS_BINARY', '/usr/bin/env compass'),
            dirname(infile),
            getattr(settings, 'PIPELINE_COMPASS_ARGUMENTS', ''),
            dirname(outfile),
            infile
        )
        return self.execute_command(command, cwd=dirname(infile))