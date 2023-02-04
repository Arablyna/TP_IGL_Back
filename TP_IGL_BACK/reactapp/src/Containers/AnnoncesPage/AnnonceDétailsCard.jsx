import React from "react";
import {IoCloseOutline, IoChatbubblesOutline, IoMailOutline, IoCallOutline, IoLocationOutline} from "react-icons/io5";
import ImageSlider from "../../Components/ImageSlider";

const AnnonceDetailsCard = ({user, annonce, closeDetails}) => {
    return (
        <div className="Overlay" onClick={() => closeDetails(false)}>
            <div className="annonceDetails" onClick={(e) => {e.stopPropagation()}}>
                <div className="Profile">
                    <div className="section">
                        <img src={user.Image.length > 0 ? user.Image : 'https://via.placeholder.com/400'}
                            alt='Profil'/>
                        <div>
                            <h2>{user.FirstName} {user.LastName}</h2>
                            <h3>{annonce.Date}</h3>
                        </div>
                    </div>
                    <button onClick={() => closeDetails(false)}><IoCloseOutline size="32px"/></button>
                </div>
                <div className="infos">
                    {
                        annonce.Poster.length > 0 ?
                        <div className="Photos">
                            <h2>Photos</h2>
                            <ImageSlider ImageList={annonce.Poster}/>
                        </div> :
                        <div className="empty">Aucune Image trouvée</div>
                    }
                    <div className="smallInfos">
                        <h2>{annonce.Price} DA</h2>
                        <h3>{annonce.Infos}</h3>
                    </div>
                    <div>
                        <h3>{annonce.Location}</h3>
                    </div>
                    <div>
                        <h2>Contact</h2>
                        <div className="section">
                            <button className="message">Message <IoChatbubblesOutline size="18px"/></button>
                            <div className="contact">
                                <button><IoCallOutline size="26px"/></button>
                                <button><IoMailOutline size="26px"/></button>
                            </div>
                        </div>
                    </div>
                    <button className="location">Afficher la localisation sur la carte<IoLocationOutline size="16px"/></button>
                </div>
            </div>
        </div>
    )
}
export default AnnonceDetailsCard;