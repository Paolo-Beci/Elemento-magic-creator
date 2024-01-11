package main

type SpecsCall struct {
	URL string `json:"url"`
}

func NewSpecs(url string) *SpecsCall {
	return &SpecsCall{
		URL: url,
	}
}