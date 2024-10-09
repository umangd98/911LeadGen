## Steps for project

1. Run script on page of archives for particular station to download audio. Login - https://www.broadcastify.com/login/
    1. Make a new folder named after station 
2. Run script on page of archives to download mapping csv 
    1. adding to the same folder 
3. Chunk audios into folders using ‘chunk_audio_directory_parallel’ or ‘chunk_audio_directory’
4. Use ‘audio_to_text_directory’ to have transcripts for all the chunks for each folder stitched and saved to a txt file. 
5. Run ‘process_file’ to generate a txt file address and context json 
6. Run ‘extractjson_tocsv.py’ for creating csv.

