# NBA Impact Calc

## What?
This project is an end-to-end ETL (Extract, Transform, Load) pipeline that ingests, processes, and analyzes NBA player data to compute a custom Impact Score for each player.

## Why?
Wanted to be a data eng - so I'm teaching myself😁

## How are players scored?
- Each stat is normalized on a 0–100 scale using league-wide min and max values.
- Turnovers and Plus-Minus are treated with custom logic to reflect their unique impact.
- Weighted scoring is applied to each stat based on its importance, producing a final Impact Score.


## Dev notes
Run build script by running `run_pipeline.py` script from inside the `data_pipeline` directory. 
Note: You'll to connect own MongoDB connection!

## The Future
- Front end (Next.js)
- AI explanation feature (🤫)
