import * as fs from "fs";
import signale from "signale";

const WORKFLOW_FOLDER = '.github/workflows';

export function listWorkflows() {
    if (!fs.existsSync(WORKFLOW_FOLDER)) {
        signale.error(`No ${WORKFLOW_FOLDER} folder found`);
        return;
    }
    fs.readdirSync(WORKFLOW_FOLDER).forEach(file => console.log(file));
}