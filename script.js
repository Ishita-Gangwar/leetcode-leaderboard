fetch('leaderboard.json')
    .then(response => response.json())
    .then(data => {
        data.sort((a, b) => b.totalSolved - a.totalSolved);
        const tbody = document.querySelector("#leaderboard tbody");

        data.forEach((user, index) => {
            const row = document.createElement("tr");
            row.innerHTML = `
        <td>${index + 1}</td>
        <td><a href="https://leetcode.com/${user.username}" target="_blank">${user.username}</a></td>
        <td>${user.totalSolved}</td>
        <td>${user.easySolved}</td>
        <td>${user.mediumSolved}</td>
        <td>${user.hardSolved}</td>
        <td>${user.contestRating}</td>
      `;
            tbody.appendChild(row);
        });
    });
