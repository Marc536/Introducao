class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      texto: "Hello World!" };

  }

  render() {
    return /*#__PURE__*/(
      React.createElement("div", { className: "center" }, /*#__PURE__*/
      React.createElement("h1", null, " ", this.state.texto, " ")));


  }}


ReactDOM.render( /*#__PURE__*/
React.createElement(App, null), document.getElementById('root'));