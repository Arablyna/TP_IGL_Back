import React from "react";
import { useState} from "react";
import logo from '../../Assets/logoSokna.png';
import { IoSearchOutline, IoChatbubblesOutline} from "react-icons/io5";
import {useSelector} from 'react-redux';

const NavBar = () => {
    const user = useSelector((state) => state.user.value);
    const [searchTerm, setSearchTerm] = useState("");
    return (
        <div className='navBar'>
            <div>
            <img src={logo}
                alt='Logo'/>
            <div className='search'>
                <input placeholder="Recherher.."
                    value={searchTerm}
                    onChange={(e) => setSearchTerm(e.target.value)}
                />
                <button><IoSearchOutline size="24px"/></button>
            </div>
            </div>
            <div>
            <button><IoChatbubblesOutline size="24px"/></button>
            <div className="Profile">
                <img src = {user.photo }
                // : 'https://via.placeholder.com/400'
                alt="Profile"
                />
                <h3>{user.nom} {user.prenom}</h3>
            </div>
            </div>
        </div>
    )
}
export default NavBar;