<%inherit file="/main.mako" />
<h1>Graphviewer</h1>
    <div id="graph" style="width:800px;height:500px;"></div>
    <table id="datalist">
        <thead>
            <th>Host</th>
            <th>Plugin</th>
            <th>Plugin instance</th>
            <th>Type</th>
            <th>Type instance</th>
            <th>dsname</th>
            <th>dstype</th>
        </thead>
        <tbody>
        </tbody>
    </table>
    <script language="javascript" type="text/javascript"
    src="/static/js/graphviewer.js">
    </script>
