import React from "react";
import { useState} from "react";
import logo from '../../Assets/logoSokna.png';
import { IoSearchOutline, IoChatbubblesOutline} from "react-icons/io5";

const NavBar = ({user}) => {
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
                <img src = {user.Image.length > 0 ? user.Image : 'https://via.placeholder.com/400'}
                alt="Profile"
                />
                <h3>{user.FirstName} {user.LastName}</h3>
            </div>
            </div>
        </div>
    )
}
export default NavBar;