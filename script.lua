local HttpService = game:GetService("HttpService")
local url = "http://localhost:5000/notify"

local Debounce = 0	

game.Workspace.Part.Touched:Connect(function(p)
	
	
	if tick() >= Debounce then 
		Debounce = tick() +1
		if p.Parent:FindFirstChild("Humanoid") then
			local char = p.Parent
			local success, response = pcall(function()
				return HttpService:GetAsync(url)
			end)

			if success then
				print("Response:")
				print(response)
			else
				warn("Error making GET request:", response)
			end
		end
	end
end)
