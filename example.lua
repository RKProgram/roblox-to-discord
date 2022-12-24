local host = "http://127.0.0.1:6666"

function send(message)
    syn.request({
        Url = host,
        Method = "POST",
        Body = message
    })
end

game.ReplicatedStorage.DefaultChatSystemChatEvents.OnMessageDoneFiltering.OnClientEvent:Connect(function(messageData)
    local speaker = game.Players[messageData.FromSpeaker]
    local message = messageData.Message
    send(speaker.DisplayName.." ("..speaker.Name.."): "..message)
end)