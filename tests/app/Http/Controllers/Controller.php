<?php

namespace App\Http\Controllers;

use Illuminate\Foundation\Bus\DispatchesJobs;
use Illuminate\Routing\Controller as BaseController;
use Illuminate\Foundation\Validation\ValidatesRequests;
use Illuminate\Foundation\Auth\Access\AuthorizesRequests;

class Controller extends BaseController
{
    use AuthorizesRequests, DispatchesJobs, ValidatesRequests;

    public function test(Request $request)
    {
        $array_var = [
            'key_one' => 'value_one',
            'key_two' => 'value_two'
        ];
        $var_three = "value_three";
        $var_four = 'value_four';
        $translations = [
            __('underscored.simpletext'),
            __("underscored.$var_three"),
            __('underscored.' . $var_four),
            __('underscored.' . $array_var['key_one']),
            __('underscored.' . $array_var["key_two"])
        ];
    }
}
