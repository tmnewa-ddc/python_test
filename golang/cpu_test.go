package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
	"github.com/stretchr/testify/mock"
)

type MockCpuInfo struct {
	mock.Mock
	CpuInfo
}

func (m *MockCpuInfo) GetNumCPU() int {
	args := m.Called()
	return args.Int(0)
}


func TestGetCpus(t *testing.T) {
	// arrange
	saved := NewCpuInfoer
	defer func() { NewCpuInfoer = saved }()

	expectCpu := 9999
	mockCpuInfo := new(MockCpuInfo)
	mockCpuInfo.On("GetNumCPU").Once().Return(expectCpu)

	NewCpuInfoer = func() CpuInfoer {
		return mockCpuInfo
	}

	// act
	result := GetCpus()

	// assert
	assertion := assert.New(t)
	assertion.Equal(expectCpu, result)
	mockCpuInfo.AssertNumberOfCalls(t, "GetNumCPU", 1)
}
