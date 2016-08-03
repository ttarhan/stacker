import yaml

from .vault import vault_constructor
from .kms import kms_simple_constructor
from .file import file_constructor

yaml.add_constructor('!vault', vault_constructor)
yaml.add_constructor('!kms', kms_simple_constructor)
yaml.add_constructor('!file', file_constructor)
