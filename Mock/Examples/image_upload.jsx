import { useState } from 'react';
import '../Examples/image_upload.css';

const ImageUpload = () =>
{
    const [file, setFile] = useState(null);
    const [color, setColor] = useState('');
    const [palette, setPalette] = useState([]);
    const [count, setCount] = useState(0);

    const handleImageUpload = (e) => {
        setFile(e.target.files[0]);
    };

    const handlePaletteCount = (e) => {
        setCount(e.target.value);
    };

    const getColor = async (e) => {
        e.preventDefault();
        const image = new FormData();
        image.append('file', file);

        const response = await fetch('http://127.0.0.1:5000/color', {
            method: 'POST',
            body: image,
        })
        .then(response => response.json())
        .then(data => {
            console.log(data);
            setColor(data);
        });
    };

    const getPalette = async (e) =>{
        e.preventDefault();
        const image = new FormData();
        image.append('file', file);

        const response = await fetch('http://127.0.0.1:5000/palette/' + count, {
            method: 'POST',
            body: image,
        })
        .then(response => response.json())
        .then(data => {
            console.log(data);
            setPalette(data);
        });
    };

    return (
        <div>
            <input type="file" onChange={handleImageUpload}/>
            <button onClick={getColor}>Get Color</button>
            <button onClick={getPalette}>Get Palette</button>
            <p>Dominant Color = {color}</p>
            <p>Image Palette = {palette}</p>
            <input type="number" onChange={handlePaletteCount}/>
        </div>
    );
};

export default ImageUpload;