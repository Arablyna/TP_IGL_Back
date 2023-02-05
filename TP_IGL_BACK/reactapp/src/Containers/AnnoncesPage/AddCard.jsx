import React, { useEffect } from "react";
import {IoCloseOutline} from "react-icons/io5";
import TextField from '@mui/material/TextField';
import SelectChoice from "../../Components/selectChoice.jsx";
import InputAdornment from '@mui/material/InputAdornment';
import { createTheme, ThemeProvider } from '@mui/material/styles';
import { useState } from "react";
import wilayasJson from '../../Assets/Wilayas.json';
import CommunesJson from '../../Assets/Communes.json';

const AddCard = ({closeAjout}) => {

    const [errors, setErrors] = useState({});

    const styleTheme = createTheme({
        palette: {
            primary: {
            main: '#BF9959',
            },
        },
    });

    useEffect(() => {
        const wila = [];
        for (let i = 0; i < wilayasJson.length; i++){
            wila.push(wilayasJson[i].id + " - " + wilayasJson[i].name);
        }
        setWilayas(wila);
    }, [wilayas]);

    const setNewCommunes = (wilaya) => {
        setSelectCommune('');
        setCommuneDisabled(wilaya == '')
        const comm = [];
        for (let i = 0; i < CommunesJson.length; i++){
            if(CommunesJson[i].wilaya_id == wilaya)
            comm.push( CommunesJson[i].post_code + " - " +  CommunesJson[i].name);
        }
        setCommunes(comm);
    };

    const setSelectedWilaya = (wilaya) => {
        setSelectWilaya(wilaya);
        setNewCommunes(wilaya.split(" ")[0]);
    }

    const handleValidation = () => {
        setErrors({})
        let err = {};
        let formIsValid = true;
    
        //Title
        if (title == '') {
          formIsValid = false;
        //   err.push("Title ne peut pas être vide");
          err["Title"] = "Title ne peut pas être vide";
        }

        //Surface
        if (/\D/.test(surface)) {
            formIsValid = false;
            // err.push("Surface ne peut contenir que des chiffres");
            err["SurfaceLetters"] = "Surface ne peut contenir que des chiffres";
        }
        if (surface == '') {
            formIsValid = false;
            // err.push("Surface ne peut pas être vide");
            err["SurfaceEmpty"] = "Surface ne peut pas être vide";
        }

        //Prix
        if (/\D/.test(prix)) {
            formIsValid = false;
            // err.push("Prix ne peut contenir que des chiffres");
            err["PrixLetters"] = "Prix ne peut contenir que des chiffres";
        }
        if (prix == '') {
            formIsValid = false;
            // err.push("Prix ne peut pas être vide");
            err["PrixEmpty"] = "Prix ne peut pas être vide";
        }

        //Lien vers Maps
        if (link == '') {
            formIsValid = false;
            // err.push("Link ne peut pas être vide");
            err["Link"] = "Link ne peut pas être vide"
        }
        console.log(err);
        setErrors(err);
        return formIsValid;
    }

    const annonceSubmit = () => {
        // e.preventDefault();

        if (handleValidation()) {
            alert("Form submitted");
            closeAjout(false);
            // Upload annonce infos to BDD
        }
    }

    const [wilayas, setWilayas] = useState([]);
    const [communes, setCommunes] = useState([]);
    const [selectWilaya, setSelectWilaya] = useState('');
    const [selectCommune, setSelectCommune] = useState('');
    const [communeDisabled, setCommuneDisabled] = useState(true);

    const [title, setTitle] = useState('');
    const [description, setDescription] = useState('');
    const [surface, setSurface] = useState('');
    const [prix, setPrix] = useState('');
    const [link, setLink] = useState('');
    return (
        <div className="Overlay" onClick={() => closeAjout(false)}>
            <div className="annonceDetails infosCard" onClick={(e) => {e.stopPropagation()}}>
                <div className="Profile">
                    <div className="section">
                        <h1>Ajouter une annonce</h1>
                    </div>
                    <button onClick={() => closeAjout(false)}><IoCloseOutline size="32px"/></button>
                </div>
                <div className="infos">
                    <ThemeProvider theme={styleTheme}>
                        <TextField label="Title" variant="outlined" required onChange={(e) => setTitle(e.target.value)} helperText={errors["Title"]}/>
                        <TextField label="Description" variant="outlined" onChange={(e) => setDescription(e.target.value)}/>
                        <TextField
                            label="Surface"
                            variant="outlined"
                            InputProps={{
                                endAdornment: <InputAdornment position="start">m<sup>2</sup></InputAdornment>,
                            }}
                            onChange={(e) => setSurface(e.target.value)}
                            required
                            helperText={errors["SurfaceEmpty"] ? errors["SurfaceEmpty"] : errors["SurfaceLetters"]}
                        />
                        <TextField
                            label="Prix"
                            variant="outlined"
                            InputProps={{
                                endAdornment: <InputAdornment position="start">DA</InputAdornment>,
                            }}
                            required
                            onChange={(e) => setPrix(e.target.value)}
                            helperText={errors["PrixEmpty"] ? errors["PrixEmpty"] : errors["PrixLetters"]}
                        />
                        <SelectChoice name="Wilaya" options={wilayas} disabled={false} setSelect={setSelectedWilaya} selected={selectWilaya}/>
                        <SelectChoice name="Commune" options={communes} disabled={communeDisabled} setSelect={setSelectCommune} selected={selectCommune}/>
                        <TextField
                            label="Lien sur Maps"
                            variant="outlined"
                            required
                            onChange={(e) => setLink(e.target.value)}
                            helperText={errors["Link"]}
                        />
                    </ThemeProvider>
                    <button className="location photos">Upload Photos</button>
                    <button className="send" onClick={() => {annonceSubmit()}}>Post Annonce</button>
                </div>
            </div>
        </div>
    )
}
export default AddCard;