from flask import Flask, request
import requests
import json

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


# TODO: temporary until all set client and crawler
@app.route('/crawl', methods=['GET'])
def crawl():
    request_body = request.get_json()
    url = 'http://0.0.0.0:6060/source-codes'
    # data = {
    #     "requestID": request_body.get('requestID'),
    #     'searchResult': [
    #         {
    #             'documentation': 'reading a file',
    #             'url': 'https://url.com',
    #             'sourceCode': [
    #                 '''import json\n''',
    #                 '''import json\n\n\n\n\n\n\n\n\n\n\n\n\n''',
    #                 '''import json\nfrom uuid import uuid4\n# you may also want''',
    #                 '''with open(fname) as f:\n    content = f.readlines()\n# you may also want to remove whitespace characters like `\\n` at the end of each line\ncontent = [x.strip() for x in content] \nprint(2)\n'''
    #             ],
    #         },
    #         {
    #             'documentation': 'When you’re working with Python, you don’t need to import a library in order to read and write files. It’s handled natively in the language, albeit in a unique manner.',
    #             'url': 'http://www.pythonforbeginners.com/files/reading-and-writing-files-in-python',
    #             'sourceCode': [
    #                 '''file_object = open(“filename”, “mode”) where\nfile_object is the variable to add the file object.''',
    #                 '''file = open("testfile.txt","w")\nfile.write("Hello World")\nfile.close()''',
    #             ],
    #         },
    #     ],
    # }
    data = {"requestID": request_body.get('requestID'), "query": "read file", "searchResult": [
        {"url": "https://msdn.microsoft.com/en-us/library/windows/desktop/aa365467(v=vs.85).aspx",
         "documentation": "EMPTY DOC", "sourceCode": [
            "\r\n\r\nBOOL WINAPI ReadFile(\r\n  _In_&Acirc;&nbsp;&Acirc;&nbsp;&Acirc;&nbsp;&Acirc;&nbsp;&Acirc;&nbsp;&Acirc;&nbsp;&Acirc;&nbsp;&Acirc;&nbsp;HANDLE &Acirc;&nbsp;&Acirc;&nbsp;&Acirc;&nbsp;&Acirc;&nbsp;&Acirc;&nbsp;&Acirc;&nbsp;hFile,\r\n  _Out_&Acirc;&nbsp;&Acirc;&nbsp;&Acirc;&nbsp;&Acirc;&nbsp;&Acirc;&nbsp;&Acirc;&nbsp;&Acirc;&nbsp;LPVOID &Acirc;&nbsp;&Acirc;&nbsp;&Acirc;&nbsp;&Acirc;&nbsp;&Acirc;&nbsp;&Acirc;&nbsp;lpBuffer,\r\n  _In_&Acirc;&nbsp;&Acirc;&nbsp;&Acirc;&nbsp;&Acirc;&nbsp;&Acirc;&nbsp;&Acirc;&nbsp;&Acirc;&nbsp;&Acirc;&nbsp;DWORD &Acirc;&nbsp;&Acirc;&nbsp;&Acirc;&nbsp;&Acirc;&nbsp;&Acirc;&nbsp;&Acirc;&nbsp;&Acirc;&nbsp;nNumberOfBytesToRead,\r\n  _Out_opt_&Acirc;&nbsp;&Acirc;&nbsp;&Acirc;&nbsp;LPDWORD &Acirc;&nbsp;&Acirc;&nbsp;&Acirc;&nbsp;&Acirc;&nbsp;&Acirc;&nbsp;lpNumberOfBytesRead,\r\n  _Inout_opt_&Acirc;&nbsp;LPOVERLAPPED lpOverlapped\r\n);\r\n\r\n"]},
        {"url": "https://nodejs.org/api/fs.html", "documentation": "EMPTY DOC", "sourceCode": [
            "const fs = require('fs');\n\nfs.unlink('/tmp/hello', (err) =&gt; {\n  if (err) throw err;\n  console.log('successfully deleted /tmp/hello');\n});\n",
            "const fs = require('fs');\n\nfs.unlinkSync('/tmp/hello');\nconsole.log('successfully deleted /tmp/hello');\n",
            "fs.rename('/tmp/hello', '/tmp/world', (err) =&gt; {\n  if (err) throw err;\n  console.log('renamed complete');\n});\nfs.stat('/tmp/world', (err, stats) =&gt; {\n  if (err) throw err;\n  console.log(`stats: ${JSON.stringify(stats)}`);\n});\n",
            "fs.rename('/tmp/hello', '/tmp/world', (err) =&gt; {\n  if (err) throw err;\n  fs.stat('/tmp/world', (err, stats) =&gt; {\n    if (err) throw err;\n    console.log(`stats: ${JSON.stringify(stats)}`);\n  });\n});\n",
            "$ cat script.js\nfunction bad() {\n  require('fs').readFile('/');\n}\nbad();\n\n$ env NODE_DEBUG=fs node script.js\nfs.js:88\n        throw backtrace;\n        ^\nError: EISDIR: illegal operation on a directory, read\n    &lt;stack trace.&gt;\n",
            "const fs = require('fs');\nconst { URL } = require('url');\nconst fileUrl = new URL('file:///tmp/hello');\n\nfs.readFileSync(fileUrl);\n",
            "// On Windows :\n\n// - WHATWG file URLs with hostname convert to UNC path\n// file://hostname/p/a/t/h/file =&gt; \\\\hostname\\p\\a\\t\\h\\file\nfs.readFileSync(new URL('file://hostname/p/a/t/h/file'));\n\n// - WHATWG file URLs with drive letters convert to absolute path\n// file:///C:/tmp/hello =&gt; C:\\tmp\\hello\nfs.readFileSync(new URL('file:///C:/tmp/hello'));\n\n// - WHATWG file URLs without hostname must have a drive letters\nfs.readFileSync(new URL('file:///notdriveletter/p/a/t/h/file'));\nfs.readFileSync(new URL('file:///c/p/a/t/h/file'));\n// TypeError [ERR_INVALID_FILE_URL_PATH]: File URL path must be absolute\n",
            "// On other platforms:\n\n// - WHATWG file URLs with hostname are unsupported\n// file://hostname/p/a/t/h/file =&gt; throw!\nfs.readFileSync(new URL('file://hostname/p/a/t/h/file'));\n// TypeError [ERR_INVALID_FILE_URL_PATH]: must be absolute\n\n// - WHATWG file URLs convert to absolute path\n// file:///tmp/hello =&gt; /tmp/hello\nfs.readFileSync(new URL('file:///tmp/hello'));\n",
            "// On Windows\nfs.readFileSync(new URL('file:///C:/p/a/t/h/%2F'));\nfs.readFileSync(new URL('file:///C:/p/a/t/h/%2f'));\n/* TypeError [ERR_INVALID_FILE_URL_PATH]: File URL path must not include encoded\n\\ or / characters */\n\n// On POSIX\nfs.readFileSync(new URL('file:///p/a/t/h/%2F'));\nfs.readFileSync(new URL('file:///p/a/t/h/%2f'));\n/* TypeError [ERR_INVALID_FILE_URL_PATH]: File URL path must not include encoded\n/ characters */\n",
            "// On Windows\nfs.readFileSync(new URL('file:///C:/path/%5C'));\nfs.readFileSync(new URL('file:///C:/path/%5c'));\n/* TypeError [ERR_INVALID_FILE_URL_PATH]: File URL path must not include encoded\n\\ or / characters */\n",
            "// Example when handled through fs.watch listener\nfs.watch('./tmp', { encoding: 'buffer' }, (eventType, filename) =&gt; {\n  if (filename) {\n    console.log(filename);\n    // Prints: &lt;Buffer ...&gt;\n  }\n});\n",
            "Stats {\n  dev: 2114,\n  ino: 48064969,\n  mode: 33188,\n  nlink: 1,\n  uid: 85,\n  gid: 100,\n  rdev: 0,\n  size: 527,\n  blksize: 4096,\n  blocks: 8,\n  atimeMs: 1318289051000.1,\n  mtimeMs: 1318289051000.1,\n  ctimeMs: 1318289051000.1,\n  birthtimeMs: 1318289051000.1,\n  atime: Mon, 10 Oct 2011 23:24:11 GMT,\n  mtime: Mon, 10 Oct 2011 23:24:11 GMT,\n  ctime: Mon, 10 Oct 2011 23:24:11 GMT,\n  birthtime: Mon, 10 Oct 2011 23:24:11 GMT }\n",
            "fs.access('/etc/passwd', fs.constants.R_OK | fs.constants.W_OK, (err) =&gt; {\n  console.log(err ? 'no access!' : 'can read/write');\n});\n",
            "fs.access('myfile', (err) =&gt; {\n  if (!err) {\n    console.error('myfile already exists');\n    return;\n  }\n\n  fs.open('myfile', 'wx', (err, fd) =&gt; {\n    if (err) throw err;\n    writeMyData(fd);\n  });\n});\n",
            "fs.open('myfile', 'wx', (err, fd) =&gt; {\n  if (err) {\n    if (err.code === 'EEXIST') {\n      console.error('myfile already exists');\n      return;\n    }\n\n    throw err;\n  }\n\n  writeMyData(fd);\n});\n",
            "fs.access('myfile', (err) =&gt; {\n  if (err) {\n    if (err.code === 'ENOENT') {\n      console.error('myfile does not exist');\n      return;\n    }\n\n    throw err;\n  }\n\n  fs.open('myfile', 'r', (err, fd) =&gt; {\n    if (err) throw err;\n    readMyData(fd);\n  });\n});\n",
            "fs.open('myfile', 'r', (err, fd) =&gt; {\n  if (err) {\n    if (err.code === 'ENOENT') {\n      console.error('myfile does not exist');\n      return;\n    }\n\n    throw err;\n  }\n\n  readMyData(fd);\n});\n",
            "fs.appendFile('message.txt', 'data to append', (err) =&gt; {\n  if (err) throw err;\n  console.log('The \"data to append\" was appended to file!');\n});\n",
            "fs.appendFile('message.txt', 'data to append', 'utf8', callback);\n",
            "const defaults = {\n  flags: 'r',\n  encoding: null,\n  fd: null,\n  mode: 0o666,\n  autoClose: true\n};\n",
            "fs.createReadStream('sample.txt', { start: 90, end: 99 });\n",
            "const defaults = {\n  flags: 'w',\n  defaultEncoding: 'utf8',\n  fd: null,\n  mode: 0o666,\n  autoClose: true\n};\n",
            "fs.exists('/etc/passwd', (exists) =&gt; {\n  console.log(exists ? 'it\\'s there' : 'no passwd!');\n});\n",
            "fs.exists('myfile', (exists) =&gt; {\n  if (exists) {\n    console.error('myfile already exists');\n  } else {\n    fs.open('myfile', 'wx', (err, fd) =&gt; {\n      if (err) throw err;\n      writeMyData(fd);\n    });\n  }\n});\n",
            "fs.open('myfile', 'wx', (err, fd) =&gt; {\n  if (err) {\n    if (err.code === 'EEXIST') {\n      console.error('myfile already exists');\n      return;\n    }\n\n    throw err;\n  }\n\n  writeMyData(fd);\n});\n",
            "fs.exists('myfile', (exists) =&gt; {\n  if (exists) {\n    fs.open('myfile', 'r', (err, fd) =&gt; {\n      readMyData(fd);\n    });\n  } else {\n    console.error('myfile does not exist');\n  }\n});\n",
            "fs.open('myfile', 'r', (err, fd) =&gt; {\n  if (err) {\n    if (err.code === 'ENOENT') {\n      console.error('myfile does not exist');\n      return;\n    }\n\n    throw err;\n  }\n\n  readMyData(fd);\n});\n",
            "console.log(fs.readFileSync('temp.txt', 'utf8'));\n// Prints: Node.js\n\n// get the file descriptor of the file to be truncated\nconst fd = fs.openSync('temp.txt', 'r+');\n\n// truncate the file to first four bytes\nfs.ftruncate(fd, 4, (err) =&gt; {\n  assert.ifError(err);\n  console.log(fs.readFileSync('temp.txt', 'utf8'));\n});\n// Prints: Node\n",
            "console.log(fs.readFileSync('temp.txt', 'utf-8'));\n// Prints: Node.js\n\n// get the file descriptor of the file to be truncated\nconst fd = fs.openSync('temp.txt', 'r+');\n\n// truncate the file to 10 bytes, whereas the actual size is 7 bytes\nfs.ftruncate(fd, 10, (err) =&gt; {\n  assert.ifError(err);\n  console.log(fs.readFileSync('temp.txt'));\n});\n// Prints: &lt;Buffer 4e 6f 64 65 2e 6a 73 00 00 00&gt;\n// ('Node.js\\0\\0\\0' in UTF8)\n",
            "fs.mkdtemp('/tmp/foo-', (err, folder) =&gt; {\n  if (err) throw err;\n  console.log(folder);\n  // Prints: /tmp/foo-itXde2\n});\n",
            "// The parent directory for the new temporary directory\nconst tmpDir = '/tmp';\n\n// This method is *INCORRECT*:\nfs.mkdtemp(tmpDir, (err, folder) =&gt; {\n  if (err) throw err;\n  console.log(folder);\n  // Will print something similar to `/tmpabc123`.\n  // Note that a new temporary directory is created\n  // at the file system root rather than *within*\n  // the /tmp directory.\n});\n\n// This method is *CORRECT*:\nconst { sep } = require('path');\nfs.mkdtemp(`${tmpDir}${sep}`, (err, folder) =&gt; {\n  if (err) throw err;\n  console.log(folder);\n  // Will print something similar to `/tmp/abc123`.\n  // A new temporary directory is created within\n  // the /tmp directory.\n});\n",
            "// macOS and Linux\nfs.open('&lt;directory&gt;', 'a+', (err, fd) =&gt; {\n  // =&gt; [Error: EISDIR: illegal operation on a directory, open &lt;directory&gt;]\n});\n\n// Windows and FreeBSD\nfs.open('&lt;directory&gt;', 'a+', (err, fd) =&gt; {\n  // =&gt; null, &lt;fd&gt;\n});\n",
            "fs.readFile('/etc/passwd', (err, data) =&gt; {\n  if (err) throw err;\n  console.log(data);\n});\n",
            "fs.readFile('/etc/passwd', 'utf8', callback);\n",
            "// macOS, Linux and Windows\nfs.readFile('&lt;directory&gt;', (err, data) =&gt; {\n  // =&gt; [Error: EISDIR: illegal operation on a directory, read &lt;directory&gt;]\n});\n\n//  FreeBSD\nfs.readFile('&lt;directory&gt;', (err, data) =&gt; {\n  // =&gt; null, &lt;data&gt;\n});\n",
            "// macOS, Linux and Windows\nfs.readFileSync('&lt;directory&gt;');\n// =&gt; [Error: EISDIR: illegal operation on a directory, read &lt;directory&gt;]\n\n//  FreeBSD\nfs.readFileSync('&lt;directory&gt;'); // =&gt; null, &lt;data&gt;\n",
            "fs.symlink('./foo', './new-port', callback);\n",
            "fs.watch('somedir', (eventType, filename) =&gt; {\n  console.log(`event type is: ${eventType}`);\n  if (filename) {\n    console.log(`filename provided: ${filename}`);\n  } else {\n    console.log('filename not provided');\n  }\n});\n",
            "fs.watchFile('message.text', (curr, prev) =&gt; {\n  console.log(`the current mtime is: ${curr.mtime}`);\n  console.log(`the previous mtime was: ${prev.mtime}`);\n});\n",
            "fs.writeFile('message.txt', 'Hello Node.js', (err) =&gt; {\n  if (err) throw err;\n  console.log('The file has been saved!');\n});\n",
            "fs.writeFile('message.txt', 'Hello Node.js', 'utf8', callback);\n"]}]}
    headers = {'Content-Type': 'application/json'}

    requests.post(url=url, data=json.dumps(data), headers=headers)

    return json.dumps({'success': True})


@app.route('/run_get')
def run_get():
    url = 'http://0.0.0.0:6060/code-recommendations'
    data = {
        'query': 'read file',
        'libs': ['flask', 'request', 'json'],
        'comments': ['122', 'todo: test'],
        'language': 'Python',
        'sites': ['stackoverflow'],
    }

    requests.request(url=url, method='GET', data=data)

    return 'get'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=1111)
