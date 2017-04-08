var React = require('react')
var ReactDOM = require('react-dom')

var PagesList = React.createClass({
    loadBooksFromServer: function(){
        $.ajax({
            url: this.props.url,
            datatype: 'json',
            cache: false,
            success: function(data) {
                this.setState({data: data});
            }.bind(this)
        })
    },

    getInitialState: function() {
        return {data: []};
    },

    componentDidMount: function() {
        this.loadBooksFromServer();
        setInterval(this.loadPagesFromServer,
                    this.props.pollInterval)
    },
    render: function() {
        if (this.state.data) {
            console.log('DATA!')
            var pageNodes = this.state.data.map(function(page){
                return <li class="list-group-item"> Page: {page.title} </li>

            })
        }
        return (
            <div>
              <div class="page-header">
                <h1>Hello <small> Usage of Django, React and Rest API!</small></h1>
                </div>
                <ul class="list-group">
                    {pageNodes}
                </ul>
            </div>
        )
    }
})

ReactDOM.render(<PagesList url='/api/' pollInterval={1000} />,
    document.getElementById('container'))
