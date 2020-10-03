# netlify-plugin-nimbella.netlify.app

<a href="https://app.netlify.com/start/deploy?repository=https://github.com/nimbella/netlify-plugin-nimbella.netlify.app&stack=nimbella" target="_blank">![Deploy to Netlify & Nimbella](.github/deploy_to_netlify_nimbella.svg)</a>

The repository has a [Python serverless function](packages/default/greet.py) which is deployed to Nimbella. And the code inside [`public/index.html`](public/index.html) is deployed to Netlify which requests the Python function for the message to display. 

Frontend: https://netlify-plugin-nimbella.netlify.app <br>
Function Endpoint: https://netlify-plugin-nimbella.netlify.app/api/default/greet <br>
Plugin repository: https://github.com/nimbella/netlify-plugin-nimbella#netlify-plugin-nimbella
