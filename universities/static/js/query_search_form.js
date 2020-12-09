$(function () {
    $('#searchForm').submit(function (e) {
        e.preventDefault();
        e.stopImmediatePropagation();
        e.stopPropagation();

        return false;
    });

    $('#searchBtn').click(function (e) {
        e.preventDefault();
        e.stopImmediatePropagation();
        e.stopPropagation();

        const query = $('#query').val()

        console.log(query)

        location.href = "/universities?query=" + encodeURIComponent(query)
    });

    const url = new URL(location.href)

    const queryQuery = url.searchParams.get("query")

    if (queryQuery != null) {
        $('#query').val(queryQuery)
    }
});
