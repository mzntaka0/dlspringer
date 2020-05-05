# dlspringer
download pdfs of springer site using a list of xslx.
This code was inspired by this article, https://note.com/sangmin/n/n70532784cc91

### Install dependencies
* poetry
```sh
pip install poetry
```

* aria2
Ubuntu
```
apt install aria2
```

macOS
```
brew install aria2
```

### Initialization
clone
```sh
git clone https://github.com/mzntaka0/dlspringer.git
cd dlspringer
```

install libraries
```sh
poetry install
```

### Download PDFs
from project root
```
cd src/dlspringer
python dl.py
```



### TODO
- [ ] create a command line tool
- [ ] dockernize
- [ ] refactorings
- [ ] multiprocessing
