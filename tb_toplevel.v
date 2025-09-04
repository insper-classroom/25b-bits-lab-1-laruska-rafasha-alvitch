module tb_toplevel;

wire [9:0] LEDR;
reg [9:0] SW;
wire [6:0] HEX0;
reg [6:0] HEX1;

initial begin
    $from_myhdl(
        SW,
        HEX1
    );
    $to_myhdl(
        LEDR,
        HEX0
    );
end

toplevel dut(
    LEDR,
    SW,
    HEX0,
    HEX1
);

endmodule
