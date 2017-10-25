from ordereddict import OrderedDict
from glob import glob
from os.path import basename
from time import gmtime, strftime
from os import getenv
DXR_FOLDER            = getenv('DXR_FOLDER', '/data/target')
PROJET_NAME           = "CMSSW"
TREES                 = OrderedDict([(PROJET_NAME,'')]+[(basename(x),'') for x in reversed(sorted(glob(DXR_FOLDER+"/trees/"+PROJET_NAME+"_*")))])
WWW_ROOT              = '/dxr'
GENERATED_DATE        = strftime("%Y-%m-%d %H:%M:%S", gmtime())
DIRECTORY_INDEX       = '.dxr-directory-index.html'
DEFAULT_TREE          = PROJET_NAME
FILTER_LANGUAGE       = 'C'
GOOGLE_ANALYTICS_KEY  = ''
