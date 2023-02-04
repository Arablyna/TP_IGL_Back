import React from "react";
import {IoCloseOutline} from "react-icons/io5";
import SelectChoice from "../../Components/selectChoice.jsx";
import DateRangeComp from "../../Components/DateRange.jsx";
import { createTheme, ThemeProvider } from '@mui/material/styles';

const styleTheme = createTheme({
    palette: {
        primary: {
        main: '#BF9959',
        },
    },
});

const FiltresCard = ({closeFiltres}) => {
    const types = ["a", "b", "c"]
    return (
        <div className="Overlay" onClick={() => closeFiltres(false)}>
            <div className="annonceDetails infosCard" onClick={(e) => {e.stopPropagation()}}>
                <div className="Profile">
                    <div className="section">
                        <h1>Filtrer les résultats</h1>
                    </div>
                    <button onClick={() => closeFiltres(false)}><IoCloseOutline size="32px"/></button>
                </div>
                <div className="infos">
                    <ThemeProvider theme={styleTheme}>
                        <SelectChoice name="Type" options={types}/>
                        <SelectChoice name="Wilaya" options={types}/>
                        <SelectChoice name="Commune" options={types}/>
                    </ThemeProvider>
                    <div>
                        <h2>Contact</h2>
                        <div className="section">
                            <h3>Plubliée entre</h3>
                            <div className="contact">
                                <DateRangeComp/>
                            </div>
                        </div>
                    </div>
                    <button className="send">Appliquer</button>
                </div>
            </div>
        </div>
    )
}
export default FiltresCard;