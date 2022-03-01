let shell;
let args;
const command = 'poetry run python -m {{ cookiecutter.project_slug }}';

switch (process.platform) {
    case 'win32':
        shell = 'cmd';
        args = ['/C', command];
        break;
    case 'linux':
    case 'darwin':
        shell = '/bin/bash';
        args = ['-c', command];
        break;
    default:
        console.warn(
            `WARNING: Unexpected platform ${process.platform}, assuming a `
            + `Unix-like system.`
        );
        shell = '/bin/bash';
        args = ['-c', command];
}

module.exports = {
    apps: [
        {
            name: '{{ cookiecutter.project_slug }}',
            script: shell,
            args: args,

            watch: false,

            min_uptime: '5s',
            max_restarts: 3,
            restart_delay: 0,
            autorestart: true
        }
    ]
};
