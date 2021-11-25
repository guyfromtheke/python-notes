from _typeshed import OpenTextModeUpdating
import os

stage = os.environ['STAGE'].upper()

output = f"we're running ins {stage}"

if stage.startswith('PROD'):
    output = "DANGER!! -" + output

print(output)