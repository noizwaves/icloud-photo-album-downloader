# icloud-photo-album-downloader

Download iCloud Photo Album metadata (i.e. photo lists)

## Usage

1.  Fetch pyicloud fork: `$ git clone https://github.com/noizwaves/pyicloud.git#albums-in-folders pyicloud`
1.  Install pyicloud fork: `$ pip3 install ./pyicloud`
1.  Save credentials to keychain: `$ icloud --username=<EMAIL_ADDRESS>`
1.  Download albums: `$ python3 download-albums.py <EMAIL_ADDRESS>`
