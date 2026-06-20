# AI-Powered Personalized Cold Email Generator

An intelligent application that automatically researches companies from an uploaded Excel spreadsheet and generates highly personalized cold emails using Google's Gemini AI and LangChain.

## Project Structure Setup

This is the initial setup of the project structure. More documentation to follow as features are implemented!

## Core Workflow

```mermaid
graph LR
    User([User]) --> Upload[Upload Excel]
    Upload --> Validate[Validate File]
    Validate --> Read[Read Leads]
    Read --> Loop{For each Lead}
    
    Loop -->|Process| Load[Load Website]
    Load --> Extract[Extract HTML]
    Extract --> Filter[Filter Content]
    Filter --> Analyze[Business Analysis Chain]
    Analyze --> Summary[Company Summary]
    Summary --> Email[Email Generation Chain]
    Email --> Store[Store Results]
    Store --> Loop
    
    Loop -->|Done| GenExcel[Generate Updated Excel]
    GenExcel --> Download([Download Excel])
```
