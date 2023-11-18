import {program} from "commander";
import {listWorkflows} from "./commands";

const packageJson = require('../package.json');

program.name('repomeister').version(packageJson.version);

function configureCommands() {
    program.command('list').description('List workflows').action(() => listWorkflows());
}

configureCommands();

program.parse(process.argv);