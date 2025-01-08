const express = require('express');
const multer = require('multer');
const path = require('path');
const fs = require('fs');
const cors = require('cors');

const app = express();

const uploadDir = path.join(__dirname, 'uploads');
if (!fs.existsSync(uploadDir)) {
    fs.mkdirSync(uploadDir);
}

const storage = multer.diskStorage({
    destination: (req, file, cb) => {
        cb(null, uploadDir);
    },
    filename: (req, file, cb) => {
        cb(null, Date.now() + path.extname(file.originalname));
    }
});

const upload = multer({ storage: storage });

app.use(cors());
app.use('/uploads', express.static(uploadDir));

app.post('/upload', upload.single('file'), (req, res) => {
    if (!req.file) {
        return res.status(400).send('No file uploaded.');
    }
    console.log('File uploaded:', req.file.filename);
    res.status(200).json({
        message: 'File uploaded successfully!',
        filePath: `/uploads/${req.file.filename}`
    });
});

app.delete('/delete/:filename', (req, res) => {
    const filePath = path.join(uploadDir, req.params.filename);
    fs.unlink(filePath, (err) => {
        if (err) {
            return res.status(500).send('Error deleting file.');
        }
        res.status(200).send('File deleted successfully.');
    });
});

app.get('/images', (req, res) => {
    fs.readdir(uploadDir, (err, files) => {
        if (err) {
            return res.status(500).send('Error reading uploads directory.');
        }
        const imagePaths = files.map(file => `/uploads/${file}`);
        res.status(200).json({ images: imagePaths });
    });
});

app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'index.html'));
});

const PORT = 3000;
app.listen(PORT, () => {
    console.log(`Server is running at http://localhost:${PORT}`);
});
