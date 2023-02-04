import * as React from 'react';
import { useState, useEffect } from "react";
import { SelectChangeEvent } from '@mui/material';
import MenuItem from '@mui/material/MenuItem';
import Select from '@mui/material/Select';
import Box from '@mui/material/Box';
import InputLabel from '@mui/material/InputLabel';
import FormControl from '@mui/material/FormControl';

const SelectChoice = ({name, options, disabled, setSelect, selected}) => {
  // const [disable, setDisable] = useState(false);

  const handleChange = (event: SelectChangeEvent) => {
    setSelect(event.target.value);
  };

  // useEffect(() => {
  //   setDisable(disabled == true && condition == '');
  // }, [disable]);

  return (
    <Box sx={{ minWidth: 20 }}>
      <FormControl fullWidth>
        <InputLabel>{name}</InputLabel>
        <Select
          // labelId="demo-simple-select-label"
          // id="demo-simple-select"
          value={selected}
          label={name}
          onChange={handleChange}
          disabled={disabled}
        >
          {
            options.map((option) => (<MenuItem key={option} value={option}>{option}</MenuItem>))
          }
        </Select>
      </FormControl>
    </Box>
  );
};
export default SelectChoice;