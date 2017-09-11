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
    data = {'query': 'read file', 'searchResult': [{'sourceCode': ['\r\n\r\nBOOL WINAPI ReadFile(\r\n  _In_&Acirc;&nbsp;&Acirc;&nbsp;&Acirc;&nbsp;&Acirc;&nbsp;&Acirc;&nbsp;&Acirc;&nbsp;&Acirc;&nbsp;&Acirc;&nbsp;HANDLE &Acirc;&nbsp;&Acirc;&nbsp;&Acirc;&nbsp;&Acirc;&nbsp;&Acirc;&nbsp;&Acirc;&nbsp;hFile,\r\n  _Out_&Acirc;&nbsp;&Acirc;&nbsp;&Acirc;&nbsp;&Acirc;&nbsp;&Acirc;&nbsp;&Acirc;&nbsp;&Acirc;&nbsp;LPVOID &Acirc;&nbsp;&Acirc;&nbsp;&Acirc;&nbsp;&Acirc;&nbsp;&Acirc;&nbsp;&Acirc;&nbsp;lpBuffer,\r\n  _In_&Acirc;&nbsp;&Acirc;&nbsp;&Acirc;&nbsp;&Acirc;&nbsp;&Acirc;&nbsp;&Acirc;&nbsp;&Acirc;&nbsp;&Acirc;&nbsp;DWORD &Acirc;&nbsp;&Acirc;&nbsp;&Acirc;&nbsp;&Acirc;&nbsp;&Acirc;&nbsp;&Acirc;&nbsp;&Acirc;&nbsp;nNumberOfBytesToRead,\r\n  _Out_opt_&Acirc;&nbsp;&Acirc;&nbsp;&Acirc;&nbsp;LPDWORD &Acirc;&nbsp;&Acirc;&nbsp;&Acirc;&nbsp;&Acirc;&nbsp;&Acirc;&nbsp;lpNumberOfBytesRead,\r\n  _Inout_opt_&Acirc;&nbsp;LPOVERLAPPED lpOverlapped\r\n);\r\n\r\n'], 'documentation': 'EMPTY DOC', 'url': 'https://msdn.microsoft.com/en-us/library/windows/desktop/aa365467(v=vs.85).aspx'}, {'sourceCode': ['\r\nThis is the content to write into file\r\nThis is the content to write into file\r\n', '\r\npackage com.mkyong;\r\n\r\nimport java.io.BufferedReader;\r\nimport java.io.FileReader;\r\nimport java.io.IOException;\r\n\r\npublic class ReadFileExample1 {\r\n\r\n\tprivate static final String FILENAME = "E:\\\\test\\\\filename.txt";\r\n\r\n\tpublic static void main(String[] args) {\r\n\r\n\t\tBufferedReader br = null;\r\n\t\tFileReader fr = null;\r\n\r\n\t\ttry {\r\n\r\n\t\t\t//br = new BufferedReader(new FileReader(FILENAME));\r\n\t\t\tfr = new FileReader(FILENAME);\r\n\t\t\tbr = new BufferedReader(fr);\r\n\r\n\t\t\tString sCurrentLine;\r\n\r\n\t\t\twhile ((sCurrentLine = br.readLine()) != null) {\r\n\t\t\t\tSystem.out.println(sCurrentLine);\r\n\t\t\t}\r\n\r\n\t\t} catch (IOException e) {\r\n\r\n\t\t\te.printStackTrace();\r\n\r\n\t\t} finally {\r\n\r\n\t\t\ttry {\r\n\r\n\t\t\t\tif (br != null)\r\n\t\t\t\t\tbr.close();\r\n\r\n\t\t\t\tif (fr != null)\r\n\t\t\t\t\tfr.close();\r\n\r\n\t\t\t} catch (IOException ex) {\r\n\r\n\t\t\t\tex.printStackTrace();\r\n\r\n\t\t\t}\r\n\r\n\t\t}\r\n\r\n\t}\r\n\r\n}\r\n', '\r\nThis is the content to write into file\r\nThis is the content to write into file\r\n', '\r\npackage com.mkyong;\r\n\r\nimport java.io.BufferedReader;\r\nimport java.io.FileReader;\r\nimport java.io.IOException;\r\n\r\npublic class ReadFileExample2 {\r\n\r\n\tprivate static final String FILENAME = "E:\\\\test\\\\filename.txt";\r\n\r\n\tpublic static void main(String[] args) {\r\n\r\n\t\ttry (BufferedReader br = new BufferedReader(new FileReader(FILENAME))) {\r\n\r\n\t\t\tString sCurrentLine;\r\n\r\n\t\t\twhile ((sCurrentLine = br.readLine()) != null) {\r\n\t\t\t\tSystem.out.println(sCurrentLine);\r\n\t\t\t}\r\n\r\n\t\t} catch (IOException e) {\r\n\t\t\te.printStackTrace();\r\n\t\t}\r\n\r\n\t}\r\n\r\n}\r\n'], 'documentation': 'EMPTY DOC', 'url': 'https://www.mkyong.com/java/how-to-read-file-from-java-bufferedreader-example/'}, {'sourceCode': ['M = dlmread(', 'M = ', 'X = magic(3);\ndlmwrite(', 'type ', '40 5 30 1.6 0.2 1.2\n15 25 35 0.6 1 1.4\n20 45 10 0.8 1.8 0.4\n  \n8 1 6\n3 5 7\n4 9 2\n', 'M = dlmread(', 'M = ', 'test max min direction\n10 27.7 12.4 12\n11 26.9 13.5 18\n12 27.4 16.9 31\n13 25.1 12.7 29  ', 'filename = ', 'M =\n\n   10.0000   27.7000   12.4000   12.0000\n   11.0000   26.9000   13.5000   18.0000\n   12.0000   27.4000   16.9000   31.0000\n   13.0000   25.1000   12.7000   29.0000', 'test max min direction\n10 27.7 12.4 12\n11 26.9 13.5 18\n12 27.4 16.9 31\n13 25.1 12.7 29  ', 'M = dlmread(', 'M =\n\n   12.0000   27.4000   16.9000   31.0000\n   13.0000   25.1000   12.7000   29.0000'], 'documentation': 'EMPTY DOC', 'url': 'https://www.mathworks.com/help/matlab/ref/dlmread.html'}, {'sourceCode': ['var ', 'func NopCloser(r ', 'func ReadAll(r ', 'Go is a general-purpose language designed with systems programming in mind.\n', 'func ReadDir(dirname ', 'func ReadFile(filename ', 'File contents: Hello, Gophers!\n', 'func TempDir(dir, prefix ', 'func TempFile(dir, prefix ', 'func WriteFile(filename '], 'documentation': 'EMPTY DOC', 'url': 'https://golang.org/pkg/io/ioutil/'}], 'requestID': request_body.get('requestID')}
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
