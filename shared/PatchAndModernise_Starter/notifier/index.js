// Legacy notification stub. Sends nothing for real; it logs the message it would send.
function buildMessage(ticket) {
  const prefix = ticket.priority === "high" ? "[URGENT] " : "";
  return prefix + "Ticket " + ticket.id + " for " + ticket.customer + " is now " + ticket.status + ".";
}

function start(port) {
  const express = require("express");
  const app = express();
  app.use(express.json());
  app.post("/notify", function (req, res) {
    const msg = buildMessage(req.body);
    console.log("SMS ->", req.body.msisdn, msg);
    res.json({ sent: true, message: msg });
  });
  return app.listen(port, function () {
    console.log("Notifier listening on port " + port);
  });
}

module.exports = { buildMessage, start };

if (require.main === module) {
  start(process.env.PORT || 4000);
}
