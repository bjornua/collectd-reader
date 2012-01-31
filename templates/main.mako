<%inherit file="/html5.mako"/>
<head>
    <title>Unavngivet hjemmeside</title>
    <link rel="stylesheet" type="text/css" href="/static/css/main.css" />
</head>
<body>
    <div id="page">
        <div id="header">
            <h1>Unavngivet hjemmeside</h1>
        </div>
        <hr/>
        <ul>
            <li><a href="${urlfor("index")}">Forside</a></li>
            <li><a href="${urlfor("testpage0")}">Testside 0</a></li>
            <li><a href="${urlfor("testpage1")}">Testside 1</a></li>
            <li><a href="${urlfor("testpage2")}">Testside 2</a></li>
            <li><a href="${urlfor("testpage3")}">Testside 3</a></li>
        </ul>
        <hr/>
        ${next.body()}
    </div>
</body>
