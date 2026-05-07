self.addEventListener('install', (e) => {
    console.log('PWA Service Worker Installed');
});
self.addEventListener('fetch', (e) => {
    // Satisfies PWA requirements
});
