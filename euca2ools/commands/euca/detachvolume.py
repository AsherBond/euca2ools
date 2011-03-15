# Software License Agreement (BSD License)
#
# Copyright (c) 2009-2011, Eucalyptus Systems, Inc.
# All rights reserved.
#
# Redistribution and use of this software in source and binary forms, with or
# without modification, are permitted provided that the following conditions
# are met:
#
#   Redistributions of source code must retain the above
#   copyright notice, this list of conditions and the
#   following disclaimer.
#
#   Redistributions in binary form must reproduce the above
#   copyright notice, this list of conditions and the
#   following disclaimer in the documentation and/or other
#   materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
# Author: Neil Soman neil@eucalyptus.com
#         Mitch Garnaat mgarnaat@eucalyptus.com

import euca2ools.commands.eucacommand
from boto.roboto.param import Param

class DetachVolume(euca2ools.commands.eucacommand.EucaCommand):

    Description = 'Detaches a volume from an instance.'
    Options = [Param(name='instance_id', short_name='i', long_name='instance',
                     optional=True, ptype='string',
                     doc="""unique id of a running instance to detach
                     the volume from."""),
               Param(name='device', short_name='d', long_name='device',
                     optional=True, ptype='string',
                     doc='local device name (inside the guest VM) to use.'),
               Param(name='force', short_name='f', long_name='force',
                     optional=True, ptype='boolean',
                     doc="""Forces detachment if the previous detachment
                     attempt did not occur cleanly""")]
    Args = [Param(name='volume_id', ptype='string',
                  doc='unique id for the volume to be detached',
                  cardinality=1, optional=False)]

    def main(self):
        volume_id = self.arguments['volume_id']
        instance_id = self.options.get('instance_id', None)
        device = self.options.get('device', None)
        force = self.options.get('force', False)
        
        euca_conn = self.make_connection_cli()
        return_code = self.make_request_cli(euca_conn,
                                            'detach_volume',
                                            volume_id=volume_id,
                                            instance_id=instance_id,
                                            device=device,
                                            force=force)
        if return_code:
            print 'VOLUME\t%s' % volume_id

