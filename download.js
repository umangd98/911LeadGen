const downloadLinks = document.querySelectorAll('#archiveTimes tbody a');



function downloadFilesSequentially(links, index) {
    if (index >= links.length) {
        console.log('All files downloaded.');
        return;
    }

    const url = links[index].href;
    const filename = url.split('/').pop();

    fetch(url)
        .then(response => {
            if (!response.ok) {
                throw new Error(`Failed to fetch ${filename}`);
            }
            return response.blob();
        })
        .then(blob => {
            const a = document.createElement('a');
            const downloadUrl = window.URL.createObjectURL(blob);
            a.href = downloadUrl;
            a.download = `${filename}.mp3`;
            document.body.appendChild(a);
            a.click();
            window.URL.revokeObjectURL(downloadUrl);
            document.body.removeChild(a);
        })
        .catch(err => {
            console.error('Error fetching file:', err);
            console.log(`Retrying ${filename}...`);
        })
        .finally(() => {
            setTimeout(() => {
                downloadFilesSequentially(links, index + 1); // Move to the next file
            }, 2000); // 2-second delay between downloads
        });
}


 console.log(downloadLinks);
    
    if (downloadLinks.length > 0) {
        downloadFilesSequentially(downloadLinks, 0);
    } else {
        console.log('No download links found.');
    }