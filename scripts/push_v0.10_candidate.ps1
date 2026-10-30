git push origin build/v0.10.0
if ($LASTEXITCODE -ne 0) { throw "Push failed" }
