/*
 * Licensed to the Apache Software Foundation (ASF) under one
 * or more contributor license agreements. See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership. The ASF licenses this file
 * to you under the Apache License, Version 2.0 (the
 * "License"); you may not use this file except in compliance
 * with the License. You may obtain a copy of the License at
 *
 *   http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing,
 * software distributed under the License is distributed on an
 * "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 * KIND, either express or implied. See the License for the
 * specific language governing permissions and limitations
 * under the License.
 */

// Automatically generated by MockGen. DO NOT EDIT!
// Source: thrift (interfaces: TProtocol)

package tests

import (
	"context"
	thrift "thrift"

	gomock "github.com/golang/mock/gomock"
)

// Mock of TProtocol interface
type MockTProtocol struct {
	ctrl     *gomock.Controller
	recorder *_MockTProtocolRecorder
}

// Recorder for MockTProtocol (not exported)
type _MockTProtocolRecorder struct {
	mock *MockTProtocol
}

func NewMockTProtocol(ctrl *gomock.Controller) *MockTProtocol {
	mock := &MockTProtocol{ctrl: ctrl}
	mock.recorder = &_MockTProtocolRecorder{mock}
	return mock
}

func (_m *MockTProtocol) EXPECT() *_MockTProtocolRecorder {
	return _m.recorder
}

func (_m *MockTProtocol) Flush(ctx context.Context) error {
	ret := _m.ctrl.Call(_m, "Flush")
	ret0, _ := ret[0].(error)
	return ret0
}

func (_mr *_MockTProtocolRecorder) Flush(ctx context.Context) *gomock.Call {
	return _mr.mock.ctrl.RecordCall(_mr.mock, "Flush")
}

func (_m *MockTProtocol) ReadBinary(ctx context.Context) ([]byte, error) {
	ret := _m.ctrl.Call(_m, "ReadBinary", ctx)
	ret0, _ := ret[0].([]byte)
	ret1, _ := ret[1].(error)
	return ret0, ret1
}

func (_mr *_MockTProtocolRecorder) ReadBinary(ctx context.Context) *gomock.Call {
	return _mr.mock.ctrl.RecordCall(_mr.mock, "ReadBinary", ctx)
}

func (_m *MockTProtocol) ReadBool(ctx context.Context) (bool, error) {
	ret := _m.ctrl.Call(_m, "ReadBool", ctx)
	ret0, _ := ret[0].(bool)
	ret1, _ := ret[1].(error)
	return ret0, ret1
}

func (_mr *_MockTProtocolRecorder) ReadBool(ctx context.Context) *gomock.Call {
	return _mr.mock.ctrl.RecordCall(_mr.mock, "ReadBool", ctx)
}

func (_m *MockTProtocol) ReadByte(ctx context.Context) (int8, error) {
	ret := _m.ctrl.Call(_m, "ReadByte", ctx)
	ret0, _ := ret[0].(int8)
	ret1, _ := ret[1].(error)
	return ret0, ret1
}

func (_mr *_MockTProtocolRecorder) ReadByte(ctx context.Context) *gomock.Call {
	return _mr.mock.ctrl.RecordCall(_mr.mock, "ReadByte", ctx)
}

func (_m *MockTProtocol) ReadDouble(ctx context.Context) (float64, error) {
	ret := _m.ctrl.Call(_m, "ReadDouble", ctx)
	ret0, _ := ret[0].(float64)
	ret1, _ := ret[1].(error)
	return ret0, ret1
}

func (_mr *_MockTProtocolRecorder) ReadDouble(ctx context.Context) *gomock.Call {
	return _mr.mock.ctrl.RecordCall(_mr.mock, "ReadDouble", ctx)
}

func (_m *MockTProtocol) ReadFieldBegin(ctx context.Context) (string, thrift.TType, int16, error) {
	ret := _m.ctrl.Call(_m, "ReadFieldBegin", ctx)
	ret0, _ := ret[0].(string)
	ret1, _ := ret[1].(thrift.TType)
	ret2, _ := ret[2].(int16)
	ret3, _ := ret[3].(error)
	return ret0, ret1, ret2, ret3
}

func (_mr *_MockTProtocolRecorder) ReadFieldBegin(ctx context.Context) *gomock.Call {
	return _mr.mock.ctrl.RecordCall(_mr.mock, "ReadFieldBegin", ctx)
}

func (_m *MockTProtocol) ReadFieldEnd(ctx context.Context) error {
	ret := _m.ctrl.Call(_m, "ReadFieldEnd", ctx)
	ret0, _ := ret[0].(error)
	return ret0
}

func (_mr *_MockTProtocolRecorder) ReadFieldEnd(ctx context.Context) *gomock.Call {
	return _mr.mock.ctrl.RecordCall(_mr.mock, "ReadFieldEnd", ctx)
}

func (_m *MockTProtocol) ReadI16(ctx context.Context) (int16, error) {
	ret := _m.ctrl.Call(_m, "ReadI16", ctx)
	ret0, _ := ret[0].(int16)
	ret1, _ := ret[1].(error)
	return ret0, ret1
}

func (_mr *_MockTProtocolRecorder) ReadI16(ctx context.Context) *gomock.Call {
	return _mr.mock.ctrl.RecordCall(_mr.mock, "ReadI16", ctx)
}

func (_m *MockTProtocol) ReadI32(ctx context.Context) (int32, error) {
	ret := _m.ctrl.Call(_m, "ReadI32", ctx)
	ret0, _ := ret[0].(int32)
	ret1, _ := ret[1].(error)
	return ret0, ret1
}

func (_mr *_MockTProtocolRecorder) ReadI32(ctx context.Context) *gomock.Call {
	return _mr.mock.ctrl.RecordCall(_mr.mock, "ReadI32", ctx)
}

func (_m *MockTProtocol) ReadI64(ctx context.Context) (int64, error) {
	ret := _m.ctrl.Call(_m, "ReadI64", ctx)
	ret0, _ := ret[0].(int64)
	ret1, _ := ret[1].(error)
	return ret0, ret1
}

func (_mr *_MockTProtocolRecorder) ReadI64(ctx context.Context) *gomock.Call {
	return _mr.mock.ctrl.RecordCall(_mr.mock, "ReadI64", ctx)
}

func (_m *MockTProtocol) ReadListBegin(ctx context.Context) (thrift.TType, int, error) {
	ret := _m.ctrl.Call(_m, "ReadListBegin", ctx)
	ret0, _ := ret[0].(thrift.TType)
	ret1, _ := ret[1].(int)
	ret2, _ := ret[2].(error)
	return ret0, ret1, ret2
}

func (_mr *_MockTProtocolRecorder) ReadListBegin(ctx context.Context) *gomock.Call {
	return _mr.mock.ctrl.RecordCall(_mr.mock, "ReadListBegin", ctx)
}

func (_m *MockTProtocol) ReadListEnd(ctx context.Context) error {
	ret := _m.ctrl.Call(_m, "ReadListEnd", ctx)
	ret0, _ := ret[0].(error)
	return ret0
}

func (_mr *_MockTProtocolRecorder) ReadListEnd(ctx context.Context) *gomock.Call {
	return _mr.mock.ctrl.RecordCall(_mr.mock, "ReadListEnd", ctx)
}

func (_m *MockTProtocol) ReadMapBegin(ctx context.Context) (thrift.TType, thrift.TType, int, error) {
	ret := _m.ctrl.Call(_m, "ReadMapBegin", ctx)
	ret0, _ := ret[0].(thrift.TType)
	ret1, _ := ret[1].(thrift.TType)
	ret2, _ := ret[2].(int)
	ret3, _ := ret[3].(error)
	return ret0, ret1, ret2, ret3
}

func (_mr *_MockTProtocolRecorder) ReadMapBegin(ctx context.Context) *gomock.Call {
	return _mr.mock.ctrl.RecordCall(_mr.mock, "ReadMapBegin", ctx)
}

func (_m *MockTProtocol) ReadMapEnd(ctx context.Context) error {
	ret := _m.ctrl.Call(_m, "ReadMapEnd", ctx)
	ret0, _ := ret[0].(error)
	return ret0
}

func (_mr *_MockTProtocolRecorder) ReadMapEnd(ctx context.Context) *gomock.Call {
	return _mr.mock.ctrl.RecordCall(_mr.mock, "ReadMapEnd", ctx)
}

func (_m *MockTProtocol) ReadMessageBegin(ctx context.Context) (string, thrift.TMessageType, int32, error) {
	ret := _m.ctrl.Call(_m, "ReadMessageBegin", ctx)
	ret0, _ := ret[0].(string)
	ret1, _ := ret[1].(thrift.TMessageType)
	ret2, _ := ret[2].(int32)
	ret3, _ := ret[3].(error)
	return ret0, ret1, ret2, ret3
}

func (_mr *_MockTProtocolRecorder) ReadMessageBegin(ctx context.Context) *gomock.Call {
	return _mr.mock.ctrl.RecordCall(_mr.mock, "ReadMessageBegin", ctx)
}

func (_m *MockTProtocol) ReadMessageEnd(ctx context.Context) error {
	ret := _m.ctrl.Call(_m, "ReadMessageEnd", ctx)
	ret0, _ := ret[0].(error)
	return ret0
}

func (_mr *_MockTProtocolRecorder) ReadMessageEnd(ctx context.Context) *gomock.Call {
	return _mr.mock.ctrl.RecordCall(_mr.mock, "ReadMessageEnd", ctx)
}

func (_m *MockTProtocol) ReadSetBegin(ctx context.Context) (thrift.TType, int, error) {
	ret := _m.ctrl.Call(_m, "ReadSetBegin", ctx)
	ret0, _ := ret[0].(thrift.TType)
	ret1, _ := ret[1].(int)
	ret2, _ := ret[2].(error)
	return ret0, ret1, ret2
}

func (_mr *_MockTProtocolRecorder) ReadSetBegin(ctx context.Context) *gomock.Call {
	return _mr.mock.ctrl.RecordCall(_mr.mock, "ReadSetBegin", ctx)
}

func (_m *MockTProtocol) ReadSetEnd(ctx context.Context) error {
	ret := _m.ctrl.Call(_m, "ReadSetEnd", ctx)
	ret0, _ := ret[0].(error)
	return ret0
}

func (_mr *_MockTProtocolRecorder) ReadSetEnd(ctx context.Context) *gomock.Call {
	return _mr.mock.ctrl.RecordCall(_mr.mock, "ReadSetEnd", ctx)
}

func (_m *MockTProtocol) ReadString(ctx context.Context) (string, error) {
	ret := _m.ctrl.Call(_m, "ReadString", ctx)
	ret0, _ := ret[0].(string)
	ret1, _ := ret[1].(error)
	return ret0, ret1
}

func (_mr *_MockTProtocolRecorder) ReadString(ctx context.Context) *gomock.Call {
	return _mr.mock.ctrl.RecordCall(_mr.mock, "ReadString", ctx)
}

func (_m *MockTProtocol) ReadStructBegin(ctx context.Context) (string, error) {
	ret := _m.ctrl.Call(_m, "ReadStructBegin", ctx)
	ret0, _ := ret[0].(string)
	ret1, _ := ret[1].(error)
	return ret0, ret1
}

func (_mr *_MockTProtocolRecorder) ReadStructBegin(ctx context.Context) *gomock.Call {
	return _mr.mock.ctrl.RecordCall(_mr.mock, "ReadStructBegin", ctx)
}

func (_m *MockTProtocol) ReadStructEnd(ctx context.Context) error {
	ret := _m.ctrl.Call(_m, "ReadStructEnd", ctx)
	ret0, _ := ret[0].(error)
	return ret0
}

func (_mr *_MockTProtocolRecorder) ReadStructEnd(ctx context.Context) *gomock.Call {
	return _mr.mock.ctrl.RecordCall(_mr.mock, "ReadStructEnd", ctx)
}

func (_m *MockTProtocol) Skip(ctx context.Context, _param0 thrift.TType) error {
	ret := _m.ctrl.Call(_m, "Skip", ctx, _param0)
	ret0, _ := ret[0].(error)
	return ret0
}

func (_mr *_MockTProtocolRecorder) Skip(ctx context.Context, arg0 interface{}) *gomock.Call {
	return _mr.mock.ctrl.RecordCall(_mr.mock, "Skip", ctx, arg0)
}

func (_m *MockTProtocol) Transport() thrift.TTransport {
	ret := _m.ctrl.Call(_m, "Transport")
	ret0, _ := ret[0].(thrift.TTransport)
	return ret0
}

func (_mr *_MockTProtocolRecorder) Transport() *gomock.Call {
	return _mr.mock.ctrl.RecordCall(_mr.mock, "Transport")
}

func (_m *MockTProtocol) WriteBinary(ctx context.Context, _param0 []byte) error {
	ret := _m.ctrl.Call(_m, "WriteBinary", ctx, _param0)
	ret0, _ := ret[0].(error)
	return ret0
}

func (_mr *_MockTProtocolRecorder) WriteBinary(ctx context.Context, arg0 interface{}) *gomock.Call {
	return _mr.mock.ctrl.RecordCall(_mr.mock, "WriteBinary", ctx, arg0)
}

func (_m *MockTProtocol) WriteBool(ctx context.Context, _param0 bool) error {
	ret := _m.ctrl.Call(_m, "WriteBool", ctx, _param0)
	ret0, _ := ret[0].(error)
	return ret0
}

func (_mr *_MockTProtocolRecorder) WriteBool(ctx context.Context, arg0 interface{}) *gomock.Call {
	return _mr.mock.ctrl.RecordCall(_mr.mock, "WriteBool", ctx, arg0)
}

func (_m *MockTProtocol) WriteByte(ctx context.Context, _param0 int8) error {
	ret := _m.ctrl.Call(_m, "WriteByte", ctx, _param0)
	ret0, _ := ret[0].(error)
	return ret0
}

func (_mr *_MockTProtocolRecorder) WriteByte(ctx context.Context, arg0 interface{}) *gomock.Call {
	return _mr.mock.ctrl.RecordCall(_mr.mock, "WriteByte", ctx, arg0)
}

func (_m *MockTProtocol) WriteDouble(ctx context.Context, _param0 float64) error {
	ret := _m.ctrl.Call(_m, "WriteDouble", ctx, _param0)
	ret0, _ := ret[0].(error)
	return ret0
}

func (_mr *_MockTProtocolRecorder) WriteDouble(ctx context.Context, arg0 interface{}) *gomock.Call {
	return _mr.mock.ctrl.RecordCall(_mr.mock, "WriteDouble", ctx, arg0)
}

func (_m *MockTProtocol) WriteFieldBegin(ctx context.Context, _param0 string, _param1 thrift.TType, _param2 int16) error {
	ret := _m.ctrl.Call(_m, "WriteFieldBegin", ctx, _param0, _param1, _param2)
	ret0, _ := ret[0].(error)
	return ret0
}

func (_mr *_MockTProtocolRecorder) WriteFieldBegin(ctx context.Context, arg0, arg1, arg2 interface{}) *gomock.Call {
	return _mr.mock.ctrl.RecordCall(_mr.mock, "WriteFieldBegin", ctx, arg0, arg1, arg2)
}

func (_m *MockTProtocol) WriteFieldEnd(ctx context.Context) error {
	ret := _m.ctrl.Call(_m, "WriteFieldEnd", ctx)
	ret0, _ := ret[0].(error)
	return ret0
}

func (_mr *_MockTProtocolRecorder) WriteFieldEnd(ctx context.Context) *gomock.Call {
	return _mr.mock.ctrl.RecordCall(_mr.mock, "WriteFieldEnd", ctx)
}

func (_m *MockTProtocol) WriteFieldStop(ctx context.Context) error {
	ret := _m.ctrl.Call(_m, "WriteFieldStop", ctx)
	ret0, _ := ret[0].(error)
	return ret0
}

func (_mr *_MockTProtocolRecorder) WriteFieldStop(ctx context.Context) *gomock.Call {
	return _mr.mock.ctrl.RecordCall(_mr.mock, "WriteFieldStop", ctx)
}

func (_m *MockTProtocol) WriteI16(ctx context.Context, _param0 int16) error {
	ret := _m.ctrl.Call(_m, "WriteI16", ctx, _param0)
	ret0, _ := ret[0].(error)
	return ret0
}

func (_mr *_MockTProtocolRecorder) WriteI16(ctx context.Context, arg0 interface{}) *gomock.Call {
	return _mr.mock.ctrl.RecordCall(_mr.mock, "WriteI16", ctx, arg0)
}

func (_m *MockTProtocol) WriteI32(ctx context.Context, _param0 int32) error {
	ret := _m.ctrl.Call(_m, "WriteI32", ctx, _param0)
	ret0, _ := ret[0].(error)
	return ret0
}

func (_mr *_MockTProtocolRecorder) WriteI32(ctx context.Context, arg0 interface{}) *gomock.Call {
	return _mr.mock.ctrl.RecordCall(_mr.mock, "WriteI32", ctx, arg0)
}

func (_m *MockTProtocol) WriteI64(ctx context.Context, _param0 int64) error {
	ret := _m.ctrl.Call(_m, "WriteI64", ctx, _param0)
	ret0, _ := ret[0].(error)
	return ret0
}

func (_mr *_MockTProtocolRecorder) WriteI64(ctx context.Context, arg0 interface{}) *gomock.Call {
	return _mr.mock.ctrl.RecordCall(_mr.mock, "WriteI64", ctx, arg0)
}

func (_m *MockTProtocol) WriteListBegin(ctx context.Context, _param0 thrift.TType, _param1 int) error {
	ret := _m.ctrl.Call(_m, "WriteListBegin", ctx, _param0, _param1)
	ret0, _ := ret[0].(error)
	return ret0
}

func (_mr *_MockTProtocolRecorder) WriteListBegin(ctx context.Context, arg0, arg1 interface{}) *gomock.Call {
	return _mr.mock.ctrl.RecordCall(_mr.mock, "WriteListBegin", ctx, arg0, arg1)
}

func (_m *MockTProtocol) WriteListEnd(ctx context.Context) error {
	ret := _m.ctrl.Call(_m, "WriteListEnd", ctx)
	ret0, _ := ret[0].(error)
	return ret0
}

func (_mr *_MockTProtocolRecorder) WriteListEnd(ctx context.Context) *gomock.Call {
	return _mr.mock.ctrl.RecordCall(_mr.mock, "WriteListEnd", ctx)
}

func (_m *MockTProtocol) WriteMapBegin(ctx context.Context, _param0 thrift.TType, _param1 thrift.TType, _param2 int) error {
	ret := _m.ctrl.Call(_m, "WriteMapBegin", ctx, _param0, _param1, _param2)
	ret0, _ := ret[0].(error)
	return ret0
}

func (_mr *_MockTProtocolRecorder) WriteMapBegin(ctx context.Context, arg0, arg1, arg2 interface{}) *gomock.Call {
	return _mr.mock.ctrl.RecordCall(_mr.mock, "WriteMapBegin", ctx, arg0, arg1, arg2)
}

func (_m *MockTProtocol) WriteMapEnd(ctx context.Context) error {
	ret := _m.ctrl.Call(_m, "WriteMapEnd", ctx)
	ret0, _ := ret[0].(error)
	return ret0
}

func (_mr *_MockTProtocolRecorder) WriteMapEnd(ctx context.Context) *gomock.Call {
	return _mr.mock.ctrl.RecordCall(_mr.mock, "WriteMapEnd", ctx)
}

func (_m *MockTProtocol) WriteMessageBegin(ctx context.Context, _param0 string, _param1 thrift.TMessageType, _param2 int32) error {
	ret := _m.ctrl.Call(_m, "WriteMessageBegin", ctx, _param0, _param1, _param2)
	ret0, _ := ret[0].(error)
	return ret0
}

func (_mr *_MockTProtocolRecorder) WriteMessageBegin(ctx context.Context, arg0, arg1, arg2 interface{}) *gomock.Call {
	return _mr.mock.ctrl.RecordCall(_mr.mock, "WriteMessageBegin", ctx, arg0, arg1, arg2)
}

func (_m *MockTProtocol) WriteMessageEnd(ctx context.Context) error {
	ret := _m.ctrl.Call(_m, "WriteMessageEnd", ctx)
	ret0, _ := ret[0].(error)
	return ret0
}

func (_mr *_MockTProtocolRecorder) WriteMessageEnd(ctx context.Context) *gomock.Call {
	return _mr.mock.ctrl.RecordCall(_mr.mock, "WriteMessageEnd", ctx)
}

func (_m *MockTProtocol) WriteSetBegin(ctx context.Context, _param0 thrift.TType, _param1 int) error {
	ret := _m.ctrl.Call(_m, "WriteSetBegin", ctx, _param0, _param1)
	ret0, _ := ret[0].(error)
	return ret0
}

func (_mr *_MockTProtocolRecorder) WriteSetBegin(ctx context.Context, arg0, arg1 interface{}) *gomock.Call {
	return _mr.mock.ctrl.RecordCall(_mr.mock, "WriteSetBegin", ctx, arg0, arg1)
}

func (_m *MockTProtocol) WriteSetEnd(ctx context.Context) error {
	ret := _m.ctrl.Call(_m, "WriteSetEnd", ctx)
	ret0, _ := ret[0].(error)
	return ret0
}

func (_mr *_MockTProtocolRecorder) WriteSetEnd(ctx context.Context) *gomock.Call {
	return _mr.mock.ctrl.RecordCall(_mr.mock, "WriteSetEnd", ctx)
}

func (_m *MockTProtocol) WriteString(ctx context.Context, _param0 string) error {
	ret := _m.ctrl.Call(_m, "WriteString", ctx, _param0)
	ret0, _ := ret[0].(error)
	return ret0
}

func (_mr *_MockTProtocolRecorder) WriteString(ctx context.Context, arg0 interface{}) *gomock.Call {
	return _mr.mock.ctrl.RecordCall(_mr.mock, "WriteString", ctx, arg0)
}

func (_m *MockTProtocol) WriteStructBegin(ctx context.Context, _param0 string) error {
	ret := _m.ctrl.Call(_m, "WriteStructBegin", ctx, _param0)
	ret0, _ := ret[0].(error)
	return ret0
}

func (_mr *_MockTProtocolRecorder) WriteStructBegin(ctx context.Context, arg0 interface{}) *gomock.Call {
	return _mr.mock.ctrl.RecordCall(_mr.mock, "WriteStructBegin", ctx, arg0)
}

func (_m *MockTProtocol) WriteStructEnd(ctx context.Context) error {
	ret := _m.ctrl.Call(_m, "WriteStructEnd", ctx)
	ret0, _ := ret[0].(error)
	return ret0
}

func (_mr *_MockTProtocolRecorder) WriteStructEnd(ctx context.Context) *gomock.Call {
	return _mr.mock.ctrl.RecordCall(_mr.mock, "WriteStructEnd", ctx)
}