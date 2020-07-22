package main

import "runtime"

type CpuInfoer interface {
	GetNumCPU() int
}

type CpuInfo struct {

}

func (s *CpuInfo) GetNumCPU() int {
	return runtime.NumCPU()
}

var NewCpuInfoer = func() CpuInfoer {
	return new(CpuInfo)
}

func GetCpus() int {
	cpuInfoer := NewCpuInfoer()
	return cpuInfoer.GetNumCPU()
}


//  GetCpus not mock
// func GetCpus() int {
// 	return runtime.NumCPU()
// }
