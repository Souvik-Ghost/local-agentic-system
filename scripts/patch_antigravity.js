/**
 * patch_antigravity.js
 * 
 * Simulated script demonstrating how Antigravity JS bundles can be 
 * patched to support a local Ollama endpoint (e.g., localhost:11434).
 * 
 * DO NOT RUN THIS without verifying paths, as Antigravity bundle locations
 * vary by operating system and build version.
 */

const fs = require('fs');
const path = require('path');

const ANTIGRAVITY_APP_DIR = process.env.AG_APP_DIR || 'C:/Program Files/Antigravity/resources/app';
const TARGET_FILES = [
    'workbench.desktop.main.js',
    'jetskiAgent/main.js'
];

function patchFile(filePath) {
    if (!fs.existsSync(filePath)) {
        console.warn(`File not found: ${filePath}`);
        return;
    }

    console.log(`Patching ${filePath}...`);
    let content = fs.readFileSync(filePath, 'utf-8');

    // Mappings based on the Technical Blueprint
    const replacements = [
        {
            search: /requestedModel:\s*["'][A-Z0-9_]+["']/g,
            replace: `requestedModel: "GOOGLE_GEMINI_INTERNAL_BYOM"`
        },
        {
            search: /apiProvider:\s*["'][A-Z0-9_]+["']/g,
            replace: `apiProvider: "API_PROVIDER_OPENAI_VERTEX"`
        },
        {
            search: /baseUrl:\s*["']https:\/\/[a-zA-Z0-9.-]+["']/g,
            replace: `baseUrl: "http://localhost:11434/v1"`
        },
        {
            search: /modelName:\s*["'][a-zA-Z0-9.-]+["']/g,
            replace: `modelName: "gemma4:31b"` // Configure desired local model here
        }
    ];

    let patched = false;
    for (const r of replacements) {
        if (content.match(r.search)) {
            content = content.replace(r.search, r.replace);
            patched = true;
        }
    }

    if (patched) {
        fs.writeFileSync(filePath, content, 'utf-8');
        console.log(`Successfully patched ${filePath}`);
    } else {
        console.log(`No matching configuration found in ${filePath}`);
    }
}

console.log("Starting Antigravity Local Model Patch...");
for (const file of TARGET_FILES) {
    // Note: Assuming these files are in specific out/ dirs inside Antigravity
    // The exact path resolution needs to be handled in a real environment
    const targetPath = path.join(ANTIGRAVITY_APP_DIR, 'out', file); 
    patchFile(targetPath);
}
console.log("Patching sequence complete.");
