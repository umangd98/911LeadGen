function downloadCSV(csv, filename) {
    const csvFile = new Blob([csv], { type: 'text/csv' });
    const downloadLink = document.createElement('a');
    downloadLink.href = window.URL.createObjectURL(csvFile);
    downloadLink.download = filename;
    downloadLink.style.display = 'none';
    document.body.appendChild(downloadLink);
    downloadLink.click();
    document.body.removeChild(downloadLink);
}

function generateCSVFromTable() {
    const rows = document.querySelectorAll('#archiveTimes tbody tr');
    let csv = 'Start Time,End Time,File Name\n'; // Header row for CSV

    rows.forEach((row) => {
        const columns = row.querySelectorAll('td');
        const startTime = columns[0].innerText;
        const endTime = columns[1].innerText.replace(/\s+Download\s+audio\s+$/, ''); // Remove extra text
        const fileName = columns[1].querySelector('a').href.split('/').pop() + '.mp3';

        csv += `"${startTime}","${endTime}","${fileName}"\n`;
    });

    downloadCSV(csv, 'audio_files.csv');
}

generateCSVFromTable();