from os.path import dirname
from django.conf import settings

from pipeline.compilers import SubProcessCompiler

class CompassCompiler(SubProcessCompiler):
    output_extension = 'css'

    def match_file(self, filename):
        return filename.endswith(('.scss', '.sass'))

    def compile_file(self, infile, outfile, outdated=False, force=False):
        command = "%s compile --boring --sass-dir=%s --css-dir=%s %s %s 1>&2" % (
            getattr(settings, 'PIPELINE_COMPASS_BINARY', '/usr/bin/env compass'),
            dirname(infile),
            dirname(outfile),
            getattr(settings, 'PIPELINE_COMPASS_ARGUMENTS', ''),
            infile
        )
        return self.execute_command(command, cwd=dirname(infile))