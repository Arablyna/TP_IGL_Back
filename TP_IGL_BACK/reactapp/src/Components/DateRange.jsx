import React from 'react';
import { useState } from 'react';
import { Box, TextField } from '@mui/material';
// import { DateRangePicker, DateRange } from '@mui/lab';

const DateRangeComp = () =>{

  // const [value, setValue] = useState<DateRange<Date>>([null, null])
  return (
    <Box minWidth= '200px'>
      {/* <DateRangePicker
        startText = 'First Date'
        endText = 'Second Date'
        value = {value}
        onChange = {(newValue) => {setValue(newValue)}}
        renderInput = {(startProps, endProps) => (
          <>
            <TextField {...startProps}/>
            <Box sx={{mx: 2}}> to </Box>
            <TextField {...endProps}/>
          </>
        )}
      /> */}
    </Box>
  );
}
export default DateRangeComp;