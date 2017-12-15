# HTML Smash

This project is an offshoot of my CraigCode1010.com project, which can be found at [project](https://github.com/greenpro/CraigCode1010) [site](https://www.craigcode1010.com). Full documentation for this 
project, including images, code, and examples can be found at [CraigCode1010.com#htmlSmash](https://www.craigcode1010.com#htmlSmash) (coming soon). This project is used to compile the site to a static HTML 
site. The project allows for multiple teplates and HTML parts to be compiled into a single static HTML page which can be easily served up from a small embedded server or quickly from a larger server with 
minimal load on the system. This project has been designed and tested on linux through Bash on Ubuntu on Windows, though it should work on any OS as it is written in python. The project currently uses python 
3.5 which comes pre-installed on most linux distros.

## Terms
These terms will apply to this and all files in the project including documentation and code.

### HTML Part (part/snippet)
These are the individual HTML snippets which will be compiled into the final HTML page. The files in my projects will end in a *.pt file extention, though this may be changed to whatever you prefer (tip: 
using the *.pt extension will allow for syntax highlighting when using vim to edit the snippets.

### Tag
A searchable identifier within the main.pt or another *.pt file which will be replaced when smash.py is run by the corresponding HTML part content. Tags are formatted as "{{ID}}" where ID is the identifier for 
the tag.

### HTML Template (template)
These templates are used to create repeated pieces of HTML code like buttons, text boxes, and headdings.

### Target Project (smash)
This will be used to refer to the HTML project to be compiled and the final output file.

## Installation
### Linux
1. Install git.
2. Clone/Fork/Download this project into a directory (I use the home directory, though any should work).
3. Done.

## Run
To run the project, go the into the folder downloaded. If you are running the project for the first time run ./config.py and fill out the questions, else skip this step. Next run ./smash.py this will compile 
the site and leave the final product in the specified folder and file.

## Smash Setup
The target project can be setup in any layout required by the user. For an example of a possible layout see the content folder of the CraigCode1010 project found 
[here](https://github.com/greenpro/CraigCode1010/tree/master/content). The tag file may is more layout specific, and should be setup as:

{
   tag: [ID] 
   template: [TEMPLATE_PATH_AND_FILE]
   part: [PART_PATH_AND_FILE]
   
   tag1: [VALUE_1]
   tag2: [VALUE_2]
   tag3: [VALUE_3]
}

The parts in brackets (including the brackets) should be replaced with the values for each. The system will ignore spaces, tabs, and extra new lines. The ID is the ID to look for in the compiling smash 
(without the '{{}}'). The template is the path and file for the template relative to the content path provided during configuration. The part is the path and file to use in the given template. This will fill 
the {{content}} tag in the template. If no part is needed 'None' (without quotes) must be used. Tag# are any other tags which must be replaced in the template and content (These tags are local to the template 
and content pair). Tags are intended to replace smaller parts of the pair like titles, ID tags, or classes. for a full example of this see tagFile.tg in the CraigCode1010 project found 
[here](https://github.com/greenpro/CraigCode1010/blob/master/tagFile.tg). 

## Files
### config.py
* This file is used to setup the configuration for the smash.py it will create a .smashrc file in the home folder.
* The project is not currenly setup to handle multiple HTML smashes (though this would not be hard). If you would like to setup multiple smashes without modifying the project simply save multiple versions of 
  the .smashrc file and switch them out.

### smash.py
* This file is the main part of the project, it will compile the final HTML file. 
* To run the script type ./smash.py and it will compile the site based on the configuration.

### gitPush.sh
* To push the project to GitHub.

### gitPull.sh
* To pull the latest version of the project from GitHub.
