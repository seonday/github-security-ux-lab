const http = require('http');
const { exec } = require('child_process');

const server = http.createServer((req, res) => {
    const url = new URL(req.url, 'http://localhost');
    const cmd = url.searchParams.get('cmd');
    
    // Command injection: HTTP 요청의 파라미터가 시스템 명령에 직접 사용됨
    exec(cmd, (error, stdout, stderr) => {
        res.writeHead(200);
        res.end(stdout);
    });
});

server.listen(3000);
