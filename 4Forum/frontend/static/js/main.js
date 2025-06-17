class ForumApp {
constructor() {
this.maxFileSize = 5 1024 1024; // 5MB
this.isPremium = false;
}

async init() {
const userStatus = await this.checkUserStatus();
if (userStatus.premium) {
this.maxFileSize = 25 1024 1024; // 25MB
this.isPremium = true;
}
}

async uploadFile(file) {
if (file.size > this.maxFileSize) {
throw new Error('Plik jest za duży');
}

const formData = new FormData();
formData.append('file', file);

const response = await fetch('/api/upload', {
method: 'POST',
body: formData,
headers: {
'Authorization': Bearer ${localStorage.getItem('token')}
}
});

return await response.json();
}

async createServer(name) {
const response = await fetch('/api/servers', {
method: 'POST',
headers: {
'Content-Type': 'application/json',
'Authorization': Bearer ${localStorage.getItem('token')}
},
body: JSON.stringify({ name })
});

return await response.json();
}
}