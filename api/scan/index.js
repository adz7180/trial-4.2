// /api/scan/index.js

import { spawn } from 'child_process';
import formidable from 'formidable';
import path from 'path';

export const config = { api: { bodyParser: false } };

export default function handler(req, res) {
  if (req.method !== 'POST') return res.status(405).json({ error: 'Method not allowed' });

  const form = formidable({ multiples: false, uploadDir: './public/uploads', keepExtensions: true });
  form.parse(req, (err, fields, files) => {
    if (err) return res.status(500).json({ error: 'Error parsing file' });

    const { filepath } = files.file;
    const outputPath = path.join(process.cwd(), 'public', 'models', 'generated.glb');
    let stdout = '';

    const py = spawn('python3', ['./api/scan/process_blueprint.py', filepath, outputPath]);
    py.stdout.on('data', d => stdout += d.toString());
    py.stderr.on('data', d => console.error(d.toString()));
    py.on('close', code => {
      if (code === 0) {
        const { suggestions } = JSON.parse(stdout);
        res.status(200).json({
          success: true,
          modelPath: '/models/generated.glb',
          suggestions
        });
      } else {
        res.status(500).json({ error: 'AI processing failed' });
      }
    });
  });
}
